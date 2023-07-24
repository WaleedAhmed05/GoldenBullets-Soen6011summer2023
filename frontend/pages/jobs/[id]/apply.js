import { useState, useEffect } from 'react'
import { useAppContext } from '@/context/AppContext'
import Header from '@/components/layout/Header'
import styles from '@/styles/ApplicationForm.module.scss'
import Link from 'next/link'
import { useRouter } from 'next/router'
import ThankYou from '@/components/jobs/ThankYou'

const ApplicationForm = () => {
	const [success, setSuccess] = useState(null)
	const [applicationData, setApplicationData] = useState({
		candidate_id: '',
		job_post_id: '',
		cv: '',
		coverLetter: ''
	})
	
	const { user, token } = useAppContext()
	const router = useRouter()

	// Get the job post ID from the URL
	const { id } = router.query
	useEffect(() => {
		if (id) {
			setApplicationData({
				...applicationData,
				job_post_id: id,
			})
		}
	}, [id])

	const handleSubmit = async (e) => {
		e.preventDefault()
		try {
			const res = await fetch(`/api/jobs/${id}/apply`, {
				method: 'POST',
				headers: {
					'Content-Type': 'application/json',
					'Authorization': `Bearer ${token}`,
				},
				body: JSON.stringify(applicationData),
			})
			const data = await res.json()
			if (res.ok && data?.status === 'pending') {
				setSuccess(data)
			} else {
				// Show application error message
				alert('There was a problem submitting your application. Please try again.')
			}
		} catch (error) {
			// Error occurred during the API request
			console.error('Error occurred during application submission:', error)
		}
	}

	return (
		<>
			{success ? (
				<ThankYou job={success.job_post} />
			) : (
				<>
					<Header />
					<main className={styles.applicationPage}>
						<div className="container">
							{!user && (
								<div className="login">
									<p>Please login to apply.</p>
								</div>
							)}
							{user ? (
								<>
									{/* If user has already applied */}
									{user?.job_applications?.some((application) => application.job_post_id === parseInt(id)) ? (
										<>
											<h1>You have already applied for this job.</h1>
											<p>You will hear back from the recruiter within 10 business days.</p>
										</>
									) : (
										<>
										<h1>Job Application Form</h1>
										{!user ? (
											<p className={styles.loginError}>There has been a problem with your login session. Please <Link href="/login">login</Link> again.</p>
										) : (
											<form onSubmit={handleSubmit} className={styles.applicationForm}>
												<div className={styles.formGroup}>
													<label htmlFor="firstName">First Name</label>
													<input
														type="text"
														id="firstName"
														name="firstName"
														value={user?.first_name || ''}
														disabled
													/>
												</div>
												<div className={styles.formGroup}>
													<label htmlFor="lastName">Last Name</label>
													<input
														type="text"
														id="lastName"
														name="lastName"
														value={user?.last_name || ''}
														disabled
													/>
												</div>
												<div className={styles.formGroup}>
													<label htmlFor="email">Email</label>
													<input
														type="email"
														id="email"
														name="email"
														value={user?.email || ''}
														disabled
													/>
												</div>
												<div className={styles.formGroup}>
													<label htmlFor="cv">CV/Resume</label>
													<input
														type="file"
														id="cv"
														name="cv"
														onChange={(e) => setApplicationData({
															...applicationData,
															cv: e.target.files[0],
														})}
														required
													/>
												</div>
												<div className={styles.formGroup}>
													<label htmlFor="coverLetter">Cover Letter (optional)</label>
													<input
														type="file"
														id="coverLetter"
														name="coverLetter"
														onChange={(e) => setApplicationData({
															...applicationData,
															coverLetter: e.target.files[0],
														})}
													/>
												</div>
												<div className={styles.formGroup}>
													<button type="submit" className="btn btn-primary">Submit Application</button>
												</div>
											</form>
										)}
									</>
									)}
								</>
							) : null}
						</div>
					</main>
				</>
			)}
		</>
	)
}

export default ApplicationForm
