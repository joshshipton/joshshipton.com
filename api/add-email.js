import { createClient } from '@supabase/supabase-js'

const supabaseUrl = 'https://rdxhiwxfooidvexdrgxs.supabase.co';
const supabaseKey = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9'; 

const supabase = createClient(supabaseUrl, supabaseKey);

module.exports = async (req, res) => {
    if (req.method === 'POST') {
      const { email } = req.body;
      const { data, error } = await supabase
        .from('emails')
        .insert([{ email }]);
        
      if (error) {
        return res.status(400).json({ error });
      }
      return res.status(200).json({ data });
    } else {
      res.status(405).end(); // Method not allowed
    }
  };