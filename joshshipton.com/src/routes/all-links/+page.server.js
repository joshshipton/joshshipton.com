import { supabase } from "$lib/supabase";

export const load = async () => {
  const { data: links, error } = await supabase
    .from("links")
    .select("*")
    ;
  if (error) throw error;
  return {
    links,
  };
};
