import { supabase } from "$lib/supabase";

export const load = async () => {
  // Fetch posts with "grappling" tag
  const { data: posts, error } = await supabase
    .from("posts")
    .select("*")
    .eq("is_draft", false)
    .contains("tags", ["grappling"]) // This checks if "tags" array contains "grappling"
    .order("date_created", { ascending: false })
    .limit(5);

  if (error) throw error;

  // Fetch popular posts with "grappling" tag
  const { data: popular_posts, popular_error } = await supabase
    .from("posts")
    .select("*")
    .eq("is_draft", false)
    .contains("tags", ["grappling"]) // This checks if "tags" array contains "grappling"
    .eq("is_popular", true)
    .order("date_created", { ascending: false })
    .limit(3);

  if (popular_error) throw popular_error;

  return {
    posts,
    popular_posts
  };
};
