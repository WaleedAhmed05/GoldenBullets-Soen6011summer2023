import Link from 'next/link'
import { useAppContext } from 'context/AppContext'
import styles from '@/styles/Header.module.scss'

const Header = () => {
	const { user } = useAppContext()
	
	return (
		<header className={styles.header}>
			<Link href='/' className={styles.headerBrand}>Concordia Career Services</Link>
			<nav className={styles.headerNav}>
				{user ? (
					<>
						{user?.type === 'employer' ? (
							<>
								<Link href='/jobs/create'>Post a job</Link>
								<Link href="/jobs/manage">Manage job posts</Link>
							</>
						) : (
							<>
								<Link href='/jobs'>Browse jobs</Link>
								<Link href='/applications'>My applications</Link>
							</>
						)}
						{/* Notification icon */}
						<Link href='/notifications'>
							<svg width="24" height="24" fill="none" viewBox="0 0 24 24">
								<path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="1.5" d="M17.25 12V10C17.25 7.1005 14.8995 4.75 12 4.75C9.10051 4.75 6.75 7.10051 6.75 10V12L4.75 16.25H19.25L17.25 12Z"></path>
								<path stroke="currentColor" strokeLinecap="round" strokeLinejoin="round" strokeWidth="1.5" d="M9 16.75C9 16.75 9 19.25 12 19.25C15 19.25 15 16.75 15 16.75"></path>
							</svg>
						</Link>
					</>
				) : (
					<Link href='/login'>Login</Link>
				)}
			</nav>
		</header>
	)
}

export default Header