import Link from 'next/link'
import { useAppContext } from 'context/AppContext'
import styles from '@/styles/Header.module.scss'

const Header = () => {
	const { user } = useAppContext()
	
	return (
		<header className={styles.header}>
			<Link href='/' className={styles.headerBrand}>Concordia Career Services</Link>
			<nav className={styles.headerNav}>
				<Link href='/jobs'>Browse jobs</Link>
				{user ? (
					<Link href='/profile'>Profile</Link>
				) : (
					<Link href='/login'>Login</Link>
				)}
			</nav>
		</header>
	)
}

export default Header