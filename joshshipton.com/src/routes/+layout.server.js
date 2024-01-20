// src/routes/+layout.server.js
export const load = async ({ locals}) => {
    const {getSession} = locals;
    return {
      session: await getSession(),
    }
  }