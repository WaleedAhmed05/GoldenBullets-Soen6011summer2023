import { useState } from 'react'
import { useRouter } from 'next/router'
import { useAppContext } from '@/context/AppContext'
import styles from '@/styles/Profile.module.scss'

const CompanyProfileForm = () => {
	const { user, token } = useAppContext()
	const [company, setCompany] = useState({
		name: '',
		description: '',
		website: '',
		industry: '',
		num_employees: 0,
	})
	const router = useRouter()

	const formHandler = async (e) => {
		try {
			e.preventDefault()
			const res = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/company`, {
				method: 'POST',
				headers: {
					Authorization: `Bearer ${token}`,
					'Content-Type': 'application/json',
				},
				body: JSON.stringify(company),
			})
			const data = await res.json()
			if (res.ok) {
				// Go to manage jobs page
				router.push('/jobs/manage')
			} else {
				console.error('Error creating company profile', data)
				alert('Error creating company profile. Please try again.')
			}
		} catch (error) {
			console.error('Error creating company profile', error)
			alert('Error creating company profile. Please try again.')
		}
	}

	return (
		<form className={styles.companyProfileForm} onSubmit={formHandler}>
			<div className={styles.formGroup}>
				<label htmlFor="name">Name</label>
				<input type="text" id="name" name="name" required value={company.name} onChange={e => setCompany({ ...company, name: e.target.value })} />
			</div>
			<div className={styles.formGroup}>
				<label htmlFor="description">Description</label>
				<textarea id="description" name="description" required value={company.description} onChange={e => setCompany({ ...company, description: e.target.value })} />
			</div>
			<div className={styles.formGroup}>
				<label htmlFor="website">Website</label>
				<input type="text" id="website" name="website" required value={company.website} onChange={e => setCompany({ ...company, website: e.target.value })} />
			</div>
			<div className={styles.formGroup}>
				<label htmlFor="industry">Industry</label>
				<input type="text" id="industry" name="industry" required value={company.industry} onChange={e => setCompany({ ...company, industry: e.target.value })} />
			</div>
			<div className={styles.formGroup}>
				<label htmlFor="name">Size/Number of employees</label>
				<input type="number" id="num_employees" name="num_employees" required value={company.num_employees} onChange={e => setCompany({ ...company, num_employees: e.target.value })} />
			</div>
			<div className={styles.formGroup}>
				<button type="submit" className="btn btn-primary">Create job</button>
			</div>
		</form>
	)
}

export default CompanyProfileForm