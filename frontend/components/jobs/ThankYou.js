import Header from '@/components/layout/Header'
import styles from '@/styles/Job.module.scss'

const ThankYou = ({ job }) => {
	return (
		<>
			<Header />
			<main className={styles.thankYouPage}>
				<div className="container">
					<h1>Your application to the job "{job?.title}" has been successful. </h1>
					<p>You will hear back from the recruiter within 10 business days.</p>
				</div>
			</main>
		</>
	)
}

export default ThankYou