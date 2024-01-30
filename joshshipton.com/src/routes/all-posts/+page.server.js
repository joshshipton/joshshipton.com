import { supabase } from "$lib/supabase";

export const load = async () => {
  const { data: posts, error } = await supabase
    .from("posts")
    .select("id, title, date_created, post_link, content_peek ")
    .eq("is_draft", false)
    .order("date_created", { ascending: false });
  if (error) throw error;

  if (error) throw error;

  return {
    posts,
  };
};
