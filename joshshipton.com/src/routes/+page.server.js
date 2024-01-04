// here on load fetch all the posts
import { supabase } from "$lib/supabase";
export const load = async () => {
  const { data: posts, error } = await supabase
    .from("posts")
    .select("id, title, date_created, post_link, content_peek ")
    .order("date_created", { ascending: false })
    .range(0, 9);
  if (error) throw error;

  return {

      posts,

  };
};


// create a form action 

export const actions = {
  addEmail: async ({ request }) => {
    try {
      const formData = await request.formData();
      const email = formData.get('email').trim();
      const name = formData.get('name').trim();

      // Simple email validation
      if (!email.match(/^\S+@\S+\.\S+$/)) {
        return { error: 'Invalid email format' };
      }

      const { error } = await supabase.from('emails').insert([{ email, name }]);
      if (error) {
        console.error('Error inserting email:', error);
        return { error: 'Failed to subscribe' };
      }

      // Set a flag in local storage
      if (typeof window !== 'undefined') {
        localStorage.setItem('subscribed', 'true');
      }

      return { success: 'Thank you for subscribing!' };
    } catch (err) {
      console.error('Unexpected error:', err);
      return { error: 'Unexpected error occurred' };
    }
  }
};