import Link from 'next/link'
import { useAppContext } from '@/context/AppContext'
import Header from '@/components/layout/Header'
import styles from '@/styles/Home.module.scss'

const Home = () => {
	const { user, logout } = useAppContext()

	return (
		<>
			<Header />
			<main>
				<div className={styles.hero}>
					<h1>Concordia Career Services</h1>
					{user ? (
						<>
							<p>Logged in as {user?.first_name}</p>
							<button type="button" onClick={logout}>Logout</button>
						</>
					) : (
						<Link href={`${process.env.NEXT_PUBLIC_API_URL}/auth/login/google`} className={styles.googleLogin}>Login with Google</Link>
					)}
				</div>
			</main>
		</>
	)
}

export default Home