import Link from 'next/link'
import Header from '@/components/layout/Header'
import styles from '@/styles/Job.module.scss'
import { prettifyJobType, addHttps } from '@/utils'

const Job = ({ job }) => {
	console.log(job)

	return (
		<>
			<Header />
			<main className={styles.jobPage}>
				<div className="container">
					{job ? (
						<div className={styles.job}>
							<div className={styles.jobInfo}>
								<h1 className={styles.jobTitle}>{job.title}</h1>
								<ul className={styles.jobMeta}>
									<li className={styles.jobMetaItem}>{job.location}</li>
									<li className={styles.jobMetaItem}>{prettifyJobType(job.job_type)}</li>
									<li className={styles.jobMetaItem}>{job.salary}</li>
								</ul>
								<div className={styles.jobDescription}>{job.description}</div>
							</div>
							<div className={styles.jobSidebar}>
								{job.company && (
									<div className={styles.companyInfo}>
										<h2 className={styles.companyName}>{job.company?.name}</h2>
										<ul className={styles.companyMeta}>
											<li className={styles.companyMetaItem}>Location: {job.company?.location || job.location}</li>
											<li className={styles.companyMetaItem}>Industry: {job.company?.industry}</li>
											<li className={styles.companyMetaItem}>Website: <a href={addHttps(job.company?.website)} target="_blank">{job.company?.website}</a></li>
											<li className={styles.companyMetaItem}>Size: {job.company?.num_employees}</li>
										</ul>
										<Link href={`/companies/${job.company.id}`} className={styles.companyProfile}>Company profile</Link>
									</div>
								)}
								<button type="button" className={styles.jobApply}>Apply for this position</button>
							</div>
						</div>
					) : (
						<p>Loading...</p>
					)}
				</div>
			</main>
		</>
	)
}

export async function getServerSideProps({ params: { id } }) {
	const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/jobs/${id}`)
	const job = await res.json()

	return {
		props: {
			job,
		},
	}
}

export default Job