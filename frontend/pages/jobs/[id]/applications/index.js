import { useState, useEffect } from 'react'
import { useAppContext } from '@/context/AppContext'
import { useRouter } from 'next/router'
import Link from 'next/link'
import Header from '@/components/layout/Header'
import styles from '@/styles/Applications.module.scss'
import { formatDate } from '@/utils'

const Applications = () => {
	const { user, token } = useAppContext()
	const [applications, setApplications] = useState([])
	const router = useRouter()

	const { id } = router.query
	const [status, setStatus] = useState('')

	const [invite, setInvite] = useState({
	date: '',
	time: '',
	location: '',
	})

	useEffect(() => {
		if (token && id && applications?.length === 0) {
			fetchApplications()
		}
	}, [token, id, applications])

	function handleClick(s) {
	  setStatus(s);
  }

	const fetchApplications = async () => {
		try {
			const response = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/jobs/${id}/applications`, {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json',
					Authorization: `Bearer ${token}`
				},
			})
			const data = await response.json()
			if (response.ok) {
				setApplications(data)
			}
		} catch (error) {
			console.error('Error fetching applications', error)
		}
	}

	const updateStatus = async (id, status) => {
		handleClick(status)
		try {
			const response = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/applications/${id}`, {
				method: 'PUT',
				headers: {
					'Content-Type': 'application/json',
					Authorization: `Bearer ${token}`
				},
				body: JSON.stringify({ status })
			})
			const data = await response.json()
			if (response.ok && data.success) {
				fetchApplications()
			}
		} catch (error) {
			console.error('Error updating application status', error)
		}
	}

	const sendInvite = async (e, id, status, invite) => {
		e.preventDefault()
		try {
			const response = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/applications/${id}`, {
				method: 'PUT',
				headers: {
					'Content-Type': 'application/json',
					Authorization: `Bearer ${token}`
				},
				body: JSON.stringify({ status, invite })
			})
			const data = await response.json()
			if (response.ok && data.success) {
				fetchApplications()
				alert('Interview invitation sent')
				// Clear form
				setInvite({
					date: '',
					time: '',
					location: '',
				})
			}
		} catch (error) {
			console.error('Error updating application status', error)
		}
	}


	return (
		<>
			<Header />
			<main className={styles.applicationsPage}>
				<div className="container">
					{!user && (
						<div className="login">
							<p>Please login to view applications.</p>
						</div>
					)}
					{user ? (
						<>
							<h1>Applications for this job post</h1>
							<div className={styles.applications}>
								{applications?.length  ? (
									applications.map(application => (
										<div key={application.id} className={styles.application}>
											<div className={styles.applicationBase}>
												<div className={styles.applicationDetails}>
													<h2 className={styles.applicantName}>
														{`${application.candidate?.first_name} ${application.candidate?.last_name}`}
														<span className={`${styles.status} ${styles[application.status]}`}>{application.status}</span>
													</h2>
													<p>Email: {application.candidate?.email}</p>
													<p>Applied on: {formatDate(application.created_at)}</p>
													<Link href={application.cv} target='_blank'>View CV</Link>
													<Link href={`/candidate/${application.candidate.id}`}>View candidate profile</Link>
												</div>
												<div className={styles.applicationButtons}>
													<button 
														type="button" 
														onClick={() => updateStatus(application.id, 'approved')}
														disabled={application.status === 'approved'}											
													>Approve</button>
													<button
														type="button"
														onClick={() => handleClick('interview')}
														disabled={application.status === 'interview'}
													>
														Ask For Interview
													</button>
													<button
														type="button" 
														onClick={() => updateStatus(application.id, 'rejected')}
														disabled={application.status === 'rejected'}
													>Reject</button>
												</div>
											</div>

											{status === 'interview' ? (<div className={styles.createInterviewForm}>

											<h3>Create a interview invitaion</h3>
											<form onSubmit={(e) => sendInvite(e, application.id, 'interview', invite)} >
												<div className={styles.formGroup}>
													<label htmlFor="date">Date:</label>
													<input type="date" id="date" name="date"
														value={invite.date}
														min="2018-01-01" max="2024-12-31"
														onChange={(e) => setInvite({ ...invite, date: e.target.value })} />
												</div>
												<div className={styles.formGroup}>
													<label htmlFor="date">Time:</label>
													<input type="time" id="time" name="time"
														value={invite.time}
														min="09:00" max="18:00"
														onChange={(e) => setInvite({ ...invite, time: e.target.value })} />
												</div>
												<div className={styles.formGroup}>
													<label htmlFor="location">location</label>
													<input type="text" id="location" name="location" required value={invite.location} onChange={(e) => setInvite({ ...invite, location: e.target.value })} />
												</div>
												<div className={styles.formGroup}>
													<button type="submit" className="btn btn-primary">Invite</button>
												</div>
											</form>
										</div>) : null}
									</div>
									))
								) : (
									<p>There are no applications for this job post yet.</p>
								)}
							</div>
						</>
					) : null}
				</div>
			</main>
		</>
	)
}

export default Applications