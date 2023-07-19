import Link from 'next/link'
import { useAppContext } from '@/context/AppContext'
import Header from '@/components/layout/Header'
import styles from '@/styles/Jobs.module.scss'
import { prettifyJobType } from '@/utils'

const Jobs = ({ jobs }) => {
	return (
		<>
			<Header />
			<main className={styles.jobsPage}>
				<div className="container">
					<h1>Browse all jobs</h1>
					<div className={styles.jobs}>
						{jobs?.length && jobs.map(job => (
							<div key={job.id} className={styles.job}>
								<Link href={`/jobs/${job.id}`}>
									<h2 className={styles.jobTitle}>{job.title}</h2>
									<p className={styles.jobCompany}>{job.company?.name}</p>
									<ul className={styles.jobMeta}>
										<li className={styles.jobMetaItem}>{job.location}</li>
										<li className={styles.jobMetaItem}>{prettifyJobType(job.job_type)}</li>
										<li className={styles.jobMetaItem}>{job.salary}</li>
									</ul>
								</Link>
								<button type="button" className={styles.jobApply}>Apply</button>
							</div>
						))}
					</div>
				</div>
			</main>
		</>
	)
}

export async function getServerSideProps() {
	const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/jobs`)
	const jobs = await res.json()

	return {
		props: {
			jobs,
		},
	}
}

export default Jobs