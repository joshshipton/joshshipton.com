import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://rdxhiwxfooidvexdrgxs.supabase.co';
const supabaseKey = process.env.SUPABASE_KEY;

const supabase = createClient(supabaseUrl, supabaseKey);

module.exports = async (req, res) => {
    if (req.method === 'POST') {
        console.log("Received POST request");

        const { email } = req.body;

        if (!email) {
            return res.status(400).json({ error: 'Email is missing' });
        }

        const { data, error } = await supabase.from('emails').insert([{ email }]);
        
        if (error) {
            return res.status(400).json({ error: `Supabase error: ${error.message}` });
        }

        return res.status(200).json({ data });
    } else {
        res.status(405).end(); // Method not allowed
    }
};
