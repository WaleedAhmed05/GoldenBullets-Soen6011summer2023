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

	useEffect(() => {
		if (token && id && applications?.length === 0) {
			fetchApplications()
		}
	}, [token, id, applications])

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
							<h1>Applications for <span>job post</span></h1>
							<div className={styles.applications}>
								{applications?.length  ? (
									applications.map(application => (
										<div key={application.id} className={styles.application}>
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
													onClick={() => updateStatus(application.id, 'rejected')}
													disabled={application.status === 'rejected'}
												>Reject</button>
											</div>
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
