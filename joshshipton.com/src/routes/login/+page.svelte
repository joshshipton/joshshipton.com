<script>
    import { goto } from '$app/navigation';

	export let data;

	const supabase = data.supabase;

    let email = '';
    let password = '';
    let loading = false;


    async function login() {
        loading = true;
        const { data, error } = await supabase.auth.signInWithPassword({ email, password });
        loading = false;
        if (error) {
            console.log(error);
        } else {
			console.log(data);
            goto('/', { replaceState: true });
        }
    }

</script>


<div class="grid lg:grid-cols-2 min-h-screen bg-white dark:bg-gray-800">
	<div class="flex flex-col justify-center p-6 sm:p-12 lg:p-24 overflow-auto">
		<div class="w-full max-w-md mx-auto">
			<div class="text-center">
				<p>If you're here you're lost. leave</p>
			</div>

			<div class="mt-8 space-y-6">

					<label
						class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70 text-black dark:text-gray-200"
						for="email"
					>
						Email
					</label>
					<input
						name="email"
						bind:value={email}
						placeholder="email"
						class="flex h-10 bg-background text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-md"
						id="email"
						required=""
						type="email"
					/>

					<div>
						<label
							class="text-sm font-medium leading-none peer-disabled:cursor-not-allowed peer-disabled:opacity-70 text-black dark:text-gray-200"
							for="password"
						>
							Password
						</label>
						<input
							placeholder="Password"
							bind:value={password}
							type="password"
							name="password"
							class="flex h-10 bg-background text-sm ring-offset-background file:border-0 file:bg-transparent file:text-sm file:font-medium placeholder:text-muted-foreground focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:cursor-not-allowed disabled:opacity-50 w-full px-3 py-2 border border-gray-300 dark:border-gray-700 rounded-md"
							id="password"
							required=""
						/>
					</div>

					<button
						class="inline-flex items-center justify-center text-sm font-medium ring-offset-background transition-colors focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 disabled:pointer-events-none disabled:opacity-50 hover:bg-primary/90 h-10 px-4 w-full bg-black text-white rounded-md py-2"
						type="button"
                        on:click={login}
					>
                    login
					</button>
			</div>
		</div>
	</div>
</div>