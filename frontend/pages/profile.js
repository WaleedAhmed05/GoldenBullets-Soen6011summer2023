import Header from '@/components/layout/Header'
import styles from '@/styles/Profile.module.scss'
import { useAppContext } from '@/context/AppContext'
import { useRouter } from 'next/router'
import { useEffect, useState } from 'react'
import CompanyProfileForm from 'components/profile/CompanyProfileForm'

const Profile = () => {
	const { user, token } = useAppContext()
	const router = useRouter()

	// Check router for url params
	const { create } = router.query

	return (
		<>
			<Header />
			<main className={styles.profilePage}>
				<div className="container">
					<h1>Update your profile</h1>
					{create === 'company' && user?.type === 'employer' && (
						<p>Before you can create a job, you need to create a company profile.</p>
					)}
					{user?.type === 'employer' ? (
						<CompanyProfileForm />
					) : (
						<p>Candidate profile form</p>
					)}
				</div>
			</main>
		</>
	)
}

export default Profile