import { useState, useEffect } from 'react'
import { useAppContext } from '@/context/AppContext'
import Header from '@/components/layout/Header'
import styles from '@/styles/CreateJob.module.scss'
import { useRouter } from 'next/router'

const EditJob = ({ data }) => {
	const { user, token } = useAppContext()
	const router = useRouter()

	const [job, setJob] = useState({
		id: data?.id || 0,
		title: data?.title || '',
		description: data?.description || '',
		location: data?.location || '',
		salary: data?.salary || '',
		job_type: data?.job_type || '',
	})

	console.log('data', data)

	useEffect(() => {
		if (data) {
			setJob({
				id: data.id,
				title: data.title,
				description: data.description,
				location: data.location,
				salary: data.salary,
				job_type: data.job_type,
			})
		}
	}, [data])

	const createJob = async (e) => {
		e.preventDefault()
		// Send a POST request to the API to create a new job
		const res = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/jobs/${job.id}`, {
			method: 'PUT',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`
			},
			body: JSON.stringify(job)
		})
		const data = await res.json()
		if (res.ok) {
			router.push(`/jobs/${data.id}`)
		}
	}

	return (
		<>
			<Header />
			<main className={styles.createJobPage}>
				<div className="container">
					<h1>Create a job</h1>
					<form onSubmit={createJob} className={styles.createJobForm}>
						<div className={styles.formGroup}>
							<label htmlFor="title">Title</label>
							<input type="text" id="title" name="title" required value={job.title} onChange={(e) => setJob({ ...job, title: e.target.value })} />
						</div>
						<div className={styles.formGroup}>
							<label htmlFor="description">Description</label>
							<textarea id="description" name="description" required value={job.description} onChange={(e) => setJob({ ...job, description: e.target.value })} />
						</div>
						<div className={styles.formGroup}>
							<label htmlFor="location">Location</label>
							<input type="text" id="location" name="location" required value={job.location} onChange={(e) => setJob({ ...job, location: e.target.value })} />
						</div>
						<div className={styles.formGroup}>
							<label htmlFor="salary">Salary</label>
							<input type="text" id="salary" name="salary" required value={job.salary} onChange={(e) => setJob({ ...job, salary: e.target.value })} />
						</div>
						<div className={styles.formGroup}>
							<label htmlFor="job_type">Job type</label>
							<select id="job_type" name="job_type" required value={job.job_type} onChange={(e) => setJob({ ...job, job_type: e.target.value })}>
								<option value="">Select a job type</option>
								<option value="full_time">Full time</option>
								<option value="part_time">Part time</option>
								<option value="contract">Contract</option>
								<option value="internship">Internship</option>
							</select>
						</div>
						<div className={styles.formGroup}>
							<button type="submit" className="btn btn-primary">Create job</button>
						</div>
					</form>
				</div>
			</main>
		</>
	)
}

export async function getServerSideProps({ params }) {
	const res = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/jobs/${params.id}`)
	const data = await res.json()
	return {
		props: {
			data
		}
	}
}

export default EditJob