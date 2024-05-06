import { supabase } from "$lib/supabase";
import { redirect } from '@sveltejs/kit';

export const load = async ({ locals, params }) => {


  const post_link = params.id;
  console.log(post_link);

  // Fetch the post using the post_link
  const { data: post, error } = await supabase
    .from("posts")
    .select("*")
    .eq("post_link", post_link)
    // show drafts, they will be like "unlisted" youtube videos, visible but only with the link
    //.eq("is_draft", false)
    .single();

  if (error) {
    console.error("Error fetching post:", error);
    throw new Error("Error fetching post");
  }

  return {
    post,
  };

}