import Link from 'next/link'
import { useState, useEffect } from 'react'
import { useAppContext } from '@/context/AppContext'
import Header from '@/components/layout/Header'
import styles from '@/styles/Jobs.module.scss'
import { prettifyJobType } from '@/utils'

const Jobs = ({ data }) => {
	const [jobs, setJobs] = useState(data)
	const [search, setSearch] = useState('')
	const { user, token } = useAppContext()

	useEffect(() => {
		setJobs(data)
	}, [data])

	// Check if user has already applied for this job
	const hasApplied = (jobId) => {
		if (!user) return false
		return user.job_applications?.some(application => application.job_post_id === jobId)
	}

	// Search jobs
	const searchJobs = async (e) => {
		e.preventDefault()
		const res = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/jobs/search?q=${search}`, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`
			}
		})
		const jobs = await res.json()
		setJobs(jobs)
	}

	return (
		<>
			<Header />
			<main className={styles.jobsPage}>
				<div className="container">
					<h1>Browse all jobs</h1>

					{/* Search */}
					<form className={styles.search} onSubmit={searchJobs}>
						<input type="text" placeholder="Search jobs" onChange={(e) => setSearch(e.target.value)} />
						<button type="submit">Search</button>
					</form>

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
								{hasApplied(job.id) ?
									<span style={{ color: '#000' }}>Applied</span>
									:
									<Link href={`/jobs/${job.id}/apply`} className={styles.jobApply}>Apply</Link>
								}
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
			data: jobs,
		},
	}
}

export default Jobs