import Link from 'next/link'
import styles from '@/styles/Header.module.scss'

const Header = () => {
	return (
		<header className={styles.header}>
			<div className={styles.headerBrand}>Concordia Career Services</div>
			<nav className={styles.headerNav}>
				<Link href='/'>Home</Link>
				<Link href='/jobs'>Browse jobs</Link>
				<Link href='/profile'>Profile</Link>
			</nav>
		</header>
	)
}

export default Header