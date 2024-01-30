import { supabase } from "$lib/supabase";

export const load = async ({ params }) => {

  // Fetch the post using the post_link
  const { data: quotes, error } = await supabase
    .from("quotes")
    .select("*");


  if (error) {
    console.error("Error fetching quotes:", error);
    throw new Error("Error fetching quotes");
  }

  return {
    quotes
  };
};
