import Link from 'next/link'
import { useAppContext } from '@/context/AppContext'

const Home = () => {
	const { user, logout } = useAppContext()

	return (
		<main>
			{user ? (
				<>
					<p>Logged in as {user?.first_name}</p>
					<button type="button" onClick={logout}>Logout</button>
				</>
			) : (
				<Link href={`${process.env.NEXT_PUBLIC_API_URL}/auth/login`}>Login with Google</Link>
			)}
		</main>
	)
}

export default Home