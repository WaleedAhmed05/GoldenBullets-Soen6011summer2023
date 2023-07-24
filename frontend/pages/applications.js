import { useState, useEffect } from 'react'
import { useAppContext } from '@/context/AppContext'
import Link from 'next/link'
import Header from '@/components/layout/Header'
import styles from '@/styles/Applications.module.scss'
import { formatDate } from '@/utils'

const Applications = () => {
	const { token } = useAppContext()
	const [applications, setApplications] = useState([])

	useEffect(() => {
		if (token && applications?.length === 0) {
			fetchApplications()
		}
	}, [token, applications])

	const fetchApplications = async () => {
		try {
			const response = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/applications`, {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json',
					Authorization: `Bearer ${token}`
				},
			})
			const data = await response.json()
			// Sort applications by date
			data.sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
			if (response.ok) {
				setApplications(data)
			}
		} catch (error) {
			console.error('Error fetching applications', error)
		}
	}

	return (
		<>
			<Header />
			<main className={styles.applicationsPage}>
				<div className="container">
					<h1>My applications</h1>
					<div className={styles.applications}>
						{applications?.length  ? (
							applications.map(application => (
								<div key={application.id} className={styles.application}>
									<div className={styles.applicationDetails}>
										<h2 className={styles.applicantName}>{application.job_post?.title}</h2>
										<p>Company: {application.job_post?.company?.name}</p>
										<p>Applied on: {formatDate(application?.created_at)}</p>
										<Link href={application?.cv} target='_blank'>View submitted CV</Link>
									</div>
									<div className={styles.applicationButtons}>
										<span className={`${styles.status} ${styles[application.status]}`}>{application.status}</span>
									</div>
								</div>
							))
						) : (
							<p>You have not applied for any job yet.</p>
						)}
					</div>
				</div>
			</main>
		</>
	)
}

export default Applications