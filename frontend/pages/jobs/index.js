import Link from 'next/link'
import { useState, useEffect } from 'react'
import { useAppContext } from '@/context/AppContext'
import Header from '@/components/layout/Header'
import styles from '@/styles/Jobs.module.scss'
import { prettifyJobType } from '@/utils'

const Jobs = ({ data, industries }) => {
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

	// Filter by job type
	const filter = async (e) => {
		e.preventDefault()
		const { name, value } = e.target
		const res = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/jobs/search?filter&${name}=${value}`, {
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

					{/* Filters */}
					<div className={styles.filters}>
						<div className={styles.filter}>
							<label htmlFor="job_type">Job type</label>
							<select name="job_type" id="job_type" onChange={(e) => filter(e)}>
								<option value="">All</option>
								<option value="full_time">Full time</option>
								<option value="part_time">Part time</option>
								<option value="contract">Contract</option>
								<option value="internship">Internship</option>
							</select>
						</div>
						<div className={styles.filter}>
							<label htmlFor="industry">Industry</label>
							<select name="industry" id="industry" onChange={(e) => filter(e)}>
								<option value="">All</option>
								{industries?.length ? industries.map(industry => (
									<option key={industry} value={industry}>{industry}</option>
								)) : null}
							</select>
						</div>
					</div>

					<div className={styles.jobs}>
						{jobs?.length ? jobs.map(job => (
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
						)) : <p>No jobs found</p>}
					</div>
				</div>
			</main>
		</>
	)
}

export async function getServerSideProps() {
	// Get all jobs
	const jobsRes = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/jobs`)
	const jobs = await jobsRes.json()

	// Get all industries
	const industriesRes = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/jobs/search/industries`)
	const industries = await industriesRes.json()
	console.log(industries)

	return {
		props: {
			data: jobs,
			industries
		},
	}
}

export default Jobs