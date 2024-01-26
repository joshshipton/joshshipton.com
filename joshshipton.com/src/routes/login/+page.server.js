// import { fail } from '@sveltejs/kit';
// import { redirect } from '@sveltejs/kit';


// export const load = async ({ locals }) => {
// 	const session = await locals.getSession();

// 	if (session) {
// 		throw redirect(303, '/');
// 	}
// }

// // export const actions = {
// //   login: async ({ request, locals: { supabase, getSession } }) => {
// //     console.log('login action');
// //     const formData = await request.formData();
// //     const email = formData.get('email');
// //     const password = formData.get('password');


// //     if (!email || !password) {
// //       return fail(400, { error: true, message: 'Email and password are required' });
// //     }

// //     const { error } = await supabase.auth.signInWithPassword({ email, password });

// //     if (error) {
// //       return fail(401, { error: true, message: error.message });
// //     } else {
// //       console.log("redirecting to home")
// //       return { status: 200, body: { success: true, redirect: '/home?source=login' } };

// //     }


// //   },

// //   signUp: async ({ request, locals: { supabase } }) => {
// //     const formData = await request.formData();
// //     const email = formData.get('email');
// //     const password = formData.get('password');

// //     if (!email || !password) {
// //       return fail(400, { error: true, message: 'Email and password are required' });
// //     }

// //     const { error } = await supabase.auth.signUp({ email, password });

// //     if (error) {
// //       return fail(400, { error: true, message: error.message });
// //     } else {
// //       console.log("redirecting to home")
// //       return { status: 200, body: { success: true, redirect: '/home?source=signup' } };
// //     }
// //   },
// // };
