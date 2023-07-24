import Link from 'next/link'
import { useState, useEffect } from 'react'
import { useAppContext } from '@/context/AppContext'
import Header from '@/components/layout/Header'
import styles from '@/styles/Jobs.module.scss'
import { prettifyJobType } from '@/utils'

const Jobs = () => {
	const { token } = useAppContext()
	const [jobs, setJobs] = useState([])

	useEffect(() => {
		if (token && jobs?.length === 0) {
			fetchJobs()
		}
	}, [token])

	const fetchJobs = async () => {
		try {
			const response = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/jobs/employer`, {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json',
					Authorization: `Bearer ${token}`
				},
			})
			const data = await response.json()
			if (response.ok) {
				setJobs(data)
			}
		} catch (error) {
			console.error('Error fetching jobs', error)
		}
	}

	return (
		<>
			<Header />
			<main className={styles.jobsPage}>
				<div className="container">
					<h1>Manage job posts</h1>
					<div className={styles.jobs}>
						{jobs?.length  ? (
							jobs.map(job => (
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
									<Link href={`/jobs/${job?.id}/edit`} className={styles.jobApply}>Edit job</Link>
									<Link href={`/jobs/${job?.id}/applications`} className={styles.viewApplications}>View applications</Link>
								</div>
							))
						) : (
							<p>You have not posted any jobs yet.</p>
						)}
					</div>
				</div>
			</main>
		</>
	)
}

export default Jobs