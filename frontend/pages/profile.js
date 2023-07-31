import { useState, useEffect } from 'react'
import { useRouter } from 'next/router'
import { useAppContext } from '@/context/AppContext'
import Header from '@/components/layout/Header'
import styles from '@/styles/Profile.module.scss'

const Profile = () => {
	const { user, token } = useAppContext()
	const [profile, setProfile] = useState({
		first_name: '',
		last_name: '',
		linkedin_url: '',
		github_url: '',
		resume_url: '',
		work_experience: [],
		education: [],
		certifications: [],
	})

	const router = useRouter()

	useEffect(() => {
		if (user) {
			setProfile({
				first_name: user.first_name,
				last_name: user.last_name,
				linkedin_url: user.linkedin_url,
				github_url: user.github_url,
				resume_url: user.resume_url,
				work_experience: user.work_experience || [],
				education: user.education || [],
				certifications: user.certifications || [],
			})
		}
	}, [user])

	const updateProfile = async (e) => {
		e.preventDefault()
		// Remove empty fields
		const profileData = Object.fromEntries(Object.entries(profile).filter(([_, v]) => v))
		console.log('profile', profileData)
		try {
			if (!user) return
			const res = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/candidate/${user.id}`, {
				method: 'PUT',
				headers: {
					'Content-Type': 'application/json',
					Authorization: `Bearer ${token}`,
				},
				body: JSON.stringify(profileData),
			})
			const data = await res.json()
			if (res.ok) {
				router.push(`/profile`)
			}
		} catch (err) {
			console.error(err)
		}
	}

	return (
		<>
			<Header />
			<main className={styles.profilePage}>
				<div className="container">
					{!user && (
						<div className="login">
							<p>Please login to view your profile.</p>
						</div>
					)}
					{user ? (
						<>
							<h1>My Profile</h1>
							<div className={styles.profile}>
								<form onSubmit={updateProfile} className={styles.profileForm}>
									<div className={styles.formGroup}>
										<label htmlFor="first_name">First name</label>
										<input type="text" id="first_name" name="first_name" required value={profile.first_name || ''} onChange={(e) => setProfile({ ...profile, first_name: e.target.value })} />
									</div>
									<div className={styles.formGroup}>
										<label htmlFor="last_name">last name</label>
										<input type="text" id="last_name" name="last_name" required value={profile.last_name || ''} onChange={(e) => setProfile({ ...profile, last_name: e.target.value })} />
									</div>
									<div className={styles.formGroup}>
										<label htmlFor="linkedin_url">LinkedIn URL</label>
										<input type="url" id="linkedin_url" name="linkedin_url" value={profile.linkedin_url || ''} onChange={(e) => setProfile({ ...profile, linkedin_url: e.target.value })} />
									</div>
									<div className={styles.formGroup}>
										<label htmlFor="github_url">GitHub URL</label>
										<input type="url" id="github_url" name="github_url" value={profile.github_url || ''} onChange={(e) => setProfile({ ...profile, github_url: e.target.value })} />
									</div>
									<div className={styles.formGroup}>
										<label htmlFor="resume">Resume</label>
										<input type="file" id="resume_url" name="resume_url" value={profile.resume_url || ''} onChange={(e) => setProfile({ ...profile, resume_url: e.target.value })} />
									</div>
									{/* Work experience */}
										<div className={styles.formGroup}>
											<label htmlFor={`work_experience`}>Work Experience</label>
											{['', '', '',].map((_, i) => (
												<textarea 
													key={i}
													type="text" 
													id={`work_experience_${i}`} 
													name={`work_experience_${i}`} 
													value={profile.work_experience?.[i] || ''}
													onChange={(e) => {
														const newWorkExperience = [...profile.work_experience]
														newWorkExperience[i] = e.target.value
														setProfile({ ...profile, work_experience: newWorkExperience })
													}}
												></textarea>
											))}
										</div>
									{/* Education */}
										<div className={styles.formGroup}>
											<label htmlFor={`education`}>Education</label>
											{['', '', '',].map((_, i) => (
												<textarea 
													key={i}
													type="text" 
													id={`education_${i}`} 
													name={`education_${i}`}
													value={profile.education?.[i] || ''}
													onChange={(e) => {
														const newEducation = [...profile.education]
														newEducation[i] = e.target.value
														setProfile({ ...profile, education: newEducation })
													}}
												></textarea>
											))}												
										</div>
									{/* Certifications */}
										<div className={styles.formGroup}>
											<label htmlFor={`certification`}>Certifications</label>
											{['', '', '',].map((_, i) => (
												<textarea 
													key={i}
													id={`certification_${i}`} 
													name={`certification_${i}`}
													value={profile.certifications?.[i] || ''}
													onChange={(e) => {
														const newCertification = [...profile.certifications]
														newCertification[i] = e.target.value
														setProfile({ ...profile, certifications: newCertification })
													}}
												></textarea>
											))}
										</div>
									<div className={styles.formGroup}>
										<button type="submit" className="btn btn-primary">Create job</button>
									</div>
								</form>
							</div>
						</>
					) : null}
				</div>
			</main>
		</>
	)
}

export default Profile