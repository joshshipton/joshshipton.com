import { supabase } from "$lib/supabase";

export const load = async ({ params }) => {
  const post_link = params.id;
  console.log(post_link);

  // Fetch the post using the post_link
  const { data: post, error } = await supabase
    .from("posts")
    .select("*")
    .eq("post_link", post_link)
    .single();

  if (error) {
    console.error("Error fetching post:", error);
    throw new Error("Error fetching post");
  }

  return {
    post,
  };
};
