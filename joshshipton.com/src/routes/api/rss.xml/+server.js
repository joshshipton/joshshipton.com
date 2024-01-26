import { supabase } from "$lib/supabase";

export const prerender = true;

export const GET = async () => {
    // Fetch posts from Supabase
    const { data, error } = await supabase
        .from('posts')
        .select('*')
        .order('date_created', { ascending: false });
    
    if (error) {
        console.error(error);
        return new Response(
            'Internal Server Error',
            {
                status: 500
            }
        );
    }

    // Format the data for the RSS feed
    const body = render(data);
    const headers = {
        'Cache-Control': `max-age=0, s-max-age=${600}`,
        'Content-Type': 'application/xml',
    };
    return new Response(
        body,
        {
            status: 200,
            headers,
        }
    );
};

const render = (posts) => `<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
<title>Posts from Joshshipton.com</title>
<description>the latest and greatest ramblings</description>
<link>https://joshshipton.com</link>
<atom:link href="https://joshshipton.com/api/rss.xml" rel="self" type="application/rss+xml"/>
${posts
    .map(
        (post) => `<item>
<guid isPermaLink="true">https://www.joshshipton.com/post/${post.post_link}</guid>
<title>${post.title}</title>
<link>https://joshshipton.com/post/${post.post_link}</link>
<description>${post.post_content}</description>
<pubDate>${new Date(post.date_created).toUTCString()}</pubDate>
</item>`
    )
    .join('')}
</channel>
</rss>
`;

