import { useState, useEffect } from 'react'
import { useAppContext } from '@/context/AppContext'
import { useRouter } from 'next/router'
import Link from 'next/link'
import Header from '@/components/layout/Header'
import styles from '@/styles/Profile.module.scss'
import { formatDate } from '@/utils'

const CandidateProfile = () => {
	const { user, token } = useAppContext()
	const [candidate, setCandidate] = useState(null)
	const router = useRouter()

	const { id } = router.query

	useEffect(() => {
		if (token && id && !candidate?.first_name) {
			fetchCandidate(id)
		}
	}, [token, id])

	const fetchCandidate = async (id) => {
		try {
			const response = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/candidate/${id}`, {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json',
					Authorization: `Bearer ${token}`
				},
			})
			const data = await response.json()
			if (response.ok) {
				console.log('candidate', data)
				setCandidate(data)
			}
		} catch (error) {
			console.error('Error fetching candidate data', error)
		}
	}

	return (
		<>
			<Header />
			<main className={styles.candidatePage}>
				<div className="container">
					{!user && (
						<div className="login">
							<p>Please login to view candidate profile.</p>
						</div>
					)}
					{user && candidate ? (
						<>
							{/* Meta */}
							<div className={styles.meta}>
								<h1>{`${candidate.first_name} ${candidate.last_name}`}</h1>
								<p className={styles.candidateEmail}>Email: {candidate.email}</p>
								{candidate.github_url ? (
									<p className={styles.url}>GitHub URL: <a href={candidate.github_url} target='_blank'>{candidate.github_url.replace('https://', '')}</a></p>
								) : null}
								{candidate.linkedin_url ? (
									<p className={styles.url}>LinkedIn URL: <a href={candidate.linkedin_url} target='_blank'>{candidate.linkedin_url.replace('https://', '')}</a></p>
								) : null}
							</div>
							{/* Work experience */}
							<div className={styles.section}>
								<h2>Work Experience</h2>
								{candidate.work_experience.length ? (
									<ul>
										{candidate.work_experience.map((exp, i) => (
											<li key={i}>{exp}</li>
										))}
									</ul>
								) : (
									<p>No work experience listed.</p>
								)}
							</div>
							{/* Education */}
							<div className={styles.section}>
								<h2>Education</h2>
								{candidate.education.length ? (
									<ul>
										{candidate.education.map((edu, i) => (
											<li key={i}>{edu}</li>
										))}
									</ul>
								) : (
									<p>No education listed.</p>
								)}
							</div>
							{/* Certifications */}
							<div className={styles.section}>
								<h2>Certifications</h2>
								{candidate.certifications.length ? (
									<ul>
										{candidate.certifications.map((cert, i) => (
											<li key={i}>{cert}</li>
										))}
									</ul>
								) : (
									<p>No certifications listed.</p>
								)}
							</div>
						</>
					) : null}
				</div>
			</main>
		</>
	)
}

export default CandidateProfile