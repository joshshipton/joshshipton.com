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
