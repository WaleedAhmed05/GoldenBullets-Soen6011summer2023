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
								<Link href='/jobs/applied'>My applications</Link>
							</>
						)}
					</>
				) : (
					<Link href='/login'>Login</Link>
				)}
			</nav>
		</header>
	)
}

export default Header