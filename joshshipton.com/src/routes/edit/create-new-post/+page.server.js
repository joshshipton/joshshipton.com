export const load = async ({ locals }) => {
    const session = await locals.getSession();

    if (!session || !session.user) {
        throw redirect(307, '/login');
    }
}