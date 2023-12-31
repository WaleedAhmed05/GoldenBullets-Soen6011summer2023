import Link from 'next/link'
import { useRouter } from 'next/router'
import { useState, useEffect } from 'react'
import { useAppContext } from '@/context/AppContext'
import Header from '@/components/layout/Header'
import styles from '@/styles/Jobs.module.scss'
import { prettifyJobType } from '@/utils'

const Jobs = ({ data, industries }) => {
	const [jobs, setJobs] = useState(data)
	const [search, setSearch] = useState('')
	const [bookmarksFetched, setBookmarksFetched] = useState(false)
	const [showingSaved, setShowingSaved] = useState(false)
	const { user, token } = useAppContext()
	const router = useRouter()

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

	// Save/Bookmark a job
	const saveJob = async (jobId) => {
		const res = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/jobs/${Number(jobId)}/save`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`
			}
		})
		const data = await res.json()
		if (data?.error) {
			alert(data.error)
		} else if (data?.message) {
			alert('Bookmark removed')
		} else {
			alert('Job bookmarked')
		}
		// Reload page
		router.reload()
	}

	useEffect(() => {
		if (user && jobs?.length) {
			// Get job bookmarks
			const savedJobs = async () => {
				const res = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/jobs/saved`, {
					method: 'GET',
					headers: {
						'Content-Type': 'application/json',
						Authorization: `Bearer ${token}`
					}
				})
				const bookmarks = await res.json()
				if (bookmarks?.length) {
					const updatedJobs = jobs.map(job => {
						if (bookmarks.some(bookmark => bookmark.job_id === job.id)) {
							return { ...job, bookmarked: true }
						}
						return job
					})
					setJobs(updatedJobs)
					setBookmarksFetched(true)
				}
			}
			if (!bookmarksFetched) {
				savedJobs()
			}
		}
	}, [user, jobs])

	const displaySavedJobs = async () => {
		// Set jobs to only where bookmarked is true
		if (showingSaved) {
			// Reload page
			router.reload()
			return
		} else {
			setJobs(jobs.filter(job => job.bookmarked))
			setShowingSaved(true)
		}
	}

	return (
		<>
			<Header />
			<main className={styles.jobsPage}>
				<div className="container">
					<div className={styles.title}>
						<h1>Browse all jobs</h1>
						{user && !showingSaved ? <button type="button" onClick={displaySavedJobs}>View saved jobs</button> : null}
						{user && showingSaved ? <button type="button" onClick={displaySavedJobs}>View all jobs</button> : null}
					</div>

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
								<div className={styles.jobActions}>
									{/* Apply to job */}
									{hasApplied(job.id) ?
										<span style={{ color: '#000' }}>Applied</span>
										:
										<Link href={`/jobs/${job.id}/apply`} className={styles.jobApply}>Apply</Link>
									}
									{/* Save job */}
									{job.bookmarked ?
										<button type="button" className={styles.saveJob} onClick={() => saveJob(job.id)}>Unsave</button>
										:
										<button type="button" className={styles.saveJob} onClick={() => saveJob(job.id)}>Save</button>
									}
								</div>
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

	return {
		props: {
			data: jobs,
			industries
		},
	}
}

export default Jobs