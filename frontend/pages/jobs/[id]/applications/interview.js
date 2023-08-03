import { useState, useEffect } from 'react'
import { useAppContext } from '@/context/AppContext'
import Header from '@/components/layout/Header'
import styles from '@/styles/CreateJob.module.scss'
import { useRouter } from 'next/router'

const CreateInvite = () => {
	const { user, token } = useAppContext()
	const router = useRouter()
	const { id } = router.query
	console.log("id= "+id)

	const [invite, setInvite] = useState({
		date: '',
		time: '',
		location: '',
	})

	useEffect(() => {
		if (user?.company_id) {
			setInvite({ ...invite, company_id: user.company_id })
		}
	}, [user])

	const createInvite = async (e) => {
		e.preventDefault()
		// Send a POST request to the API to create a new job
		const res = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/jobs/applications/${id}/interview`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`
			},
			body: JSON.stringify(invite)
		})
		const data = await res.json()
		if (res.ok) {
			console.log(data)
		}
	}

	return (
		<>
			<Header />
			<main className={styles.createJobPage}>
				<div className="container">
					{!user && (
						<div className="login">
							<p>Please login to Send invitaion for an interview.</p>
						</div>
					)}
					{user ? (

						<>
							<h1>Create a interview invitaion</h1>
							<form onSubmit={createInvite} className={styles.createJobForm}>
								<div className={styles.formGroup}>
									<label htmlFor="start">Date:</label>
									<input type="date" id="start" name="trip-start"
										   value={invite.date}
										   min="2018-01-01" max="2024-12-31"
										   onChange={(e) => setInvite({ ...invite, date: e.target.value })} />

									<label htmlFor="appt">Time:</label>
									<input type="time" id="appt" name="appt"
										   value={invite.time}
										   min="09:00" max="18:00"
										   onChange={(e) => setInvite({ ...invite, time: e.target.value })} />

									<label htmlFor="location">location</label>
									<input type="text" id="location" name="location" required value={invite.location} onChange={(e) => setInvite({ ...invite, location: e.target.value })} />
								</div>
								<div className={styles.formGroup}>
									<button type="submit" className="btn btn-primary">Invite</button>
								</div>
							</form>
						</>
					) : null}
				</div>
			</main>
		</>
	)
}

export default CreateInvite