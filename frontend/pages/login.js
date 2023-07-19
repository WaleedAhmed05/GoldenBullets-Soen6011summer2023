import Link from 'next/link'
import Header from '@/components/layout/Header'
import styles from '@/styles/Login.module.scss'
import { useAppContext } from 'context/AppContext'
import { useRouter } from 'next/router'
import { useEffect } from 'react'

const Login = () => {
	const { user } = useAppContext()

	// If user is logged in, redirect to homepage
	const router = useRouter()
	
	useEffect(() => {
		if (user) {
			router.push('/')
		}
	}, [user])

	return (
		<>
			<Header />
			<main>
				<div className={styles.login}>
					<div className={styles.loginEmployer}>
						<h2>Want to hire?</h2>
						<p>Sign up as an employer to post jobs</p>
						<Link href={`${process.env.NEXT_PUBLIC_API_URL}/auth/login?type=employer`} className={styles.googleLogin}>Signup/Login as an employer</Link>
					</div>
					<div className={styles.loginCandidate}>
						<h2>Looking for a job?</h2>
						<p>Sign up as a candidate to apply for jobs</p>
						<Link href={`${process.env.NEXT_PUBLIC_API_URL}/auth/login?type=candidate`} className={styles.googleLogin}>Signup/Login as a candidate</Link>
					</div>
				</div>
			</main>
		</>
	)
}

export default Login