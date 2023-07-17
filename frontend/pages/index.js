import Header from '@/components/layout/Header'
import styles from '@/styles/Home.module.scss'

const Home = () => {
	return (
		<>
			<Header />
			<main>
				<div className={styles.hero}>
					<h1>Concordia Career Services</h1>
				</div>
			</main>
		</>
	)
}

export default Home