import { redirect, fail } from '@sveltejs/kit';
import { supabase } from "$lib/supabase";

export const actions = {
    update: async ({ request }) => {
        try {
            const formData = await request.formData();
            const quoteContent = formData.get('quoteContent');
            const quoteAuthor = formData.get('quoteAuthor');
            const quoteSource = formData.get('quoteSource');

            console.log('Quote Content:', quoteContent);
            console.log('Quote Author:', quoteAuthor);
            console.log('Quote Source:', quoteSource);

            // Inserting quote
            const insertedQuote = await supabase.from("quotes").insert({
                content: quoteContent,
                author: quoteAuthor,
                source: quoteSource || null
            });

            if (insertedQuote.error) {
                console.error('Error inserting quote:', insertedQuote.error);
                return fail(500, { message: 'Failed to insert quote' });
            }

            return { success: true };
        } catch (error) {
            console.error('Error in update action:', error);
            return fail(500, { message: 'An unexpected error occurred' });
        }
    }
};