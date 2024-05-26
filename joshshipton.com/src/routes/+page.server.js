// here on load fetch all the posts
import { supabase } from "$lib/supabase";

export const load = async () => {
  const { data: posts, error } = await supabase
    .from("posts")
    .select("*")
    .eq("is_draft", false)
    .order("date_created", { ascending: false })
    .limit(5);

  if (error) throw error;

  const { data: popular_posts, popular_error } = await supabase
  .from("posts")
  .select("*")
  .eq("is_draft", false)
  .eq("is_popular", true)
  .order("date_created", { ascending: false })
  .limit(3);

if (error) throw error;

  const { data: links , links_error } = await supabase
  .from("links")
  .select("*")
  .order("created_at", { ascending: false })
  .limit(18);

if (error) throw error;



if(popular_error) throw popular_error;

  return {
    posts, popular_posts,links
  };
};

// create a form action

export const actions = {
  addEmail: async ({ request }) => {
    try {
      const formData = await request.formData();
      const email = formData.get("email").trim();
      const name = formData.get("name").trim();


      console.log(name, email)

      // Simple email validation
      if (!email.match(/^\S+@\S+\.\S+$/)) {
        return { error: "Invalid email format" };
      }

      const emailResponse = await supabase
        .from("subs")
        .insert({
          email: email,
          name: name,
        })
        .single();

      if (emailResponse.error) {
        console.log(emailResponse.error);
      }

      // Set a flag in local storage
      if (typeof window !== "undefined") {
        localStorage.setItem("subscribed", "true");
      }

      return { success: "Thank you for subscribing!" };
    } catch (err) {
      console.error("Unexpected error:", err);
      return { error: "Unexpected error occurred" };
    }
  },
};
