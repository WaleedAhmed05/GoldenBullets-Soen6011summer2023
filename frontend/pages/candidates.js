import Link from 'next/link'
import { useRouter } from 'next/router'
import { useState, useEffect } from 'react'
import { useAppContext } from '@/context/AppContext'
import Header from '@/components/layout/Header'
import styles from '@/styles/Jobs.module.scss'
import { joinName } from '@/utils'

const Candidates = ({ skills }) => {
	const [candidates, setCandidates] = useState([])
	const [search, setSearch] = useState('')
	const [bookmarksFetched, setBookmarksFetched] = useState(false)
	const [showingSaved, setShowingSaved] = useState(false)
	const [showInviteForm, setShowInviteForm] = useState(0)
	const [inviteForm, setInviteForm] = useState({
		candidate_id: '',
		job_id: '',
	})
	const { user, token } = useAppContext()
	const router = useRouter()

	// Get candidates from API
	useEffect(() => {
		const fetchCandidates = async () => {
			const res = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/candidate`, {
				method: 'GET',
				headers: {
					'Content-Type': 'application/json',
					Authorization: `Bearer ${token}`
				}
			})
			const data = await res.json()
			setCandidates(data)
		}
		if (user && !candidates.length) {
			fetchCandidates()
		}
	}, [user])

	// Search candidates
	const searchJobs = async (e) => {
		e.preventDefault()
		if (search === '') {
			// Reload page
			router.reload()
			return
		}
		// Filter `candidates` by search query. Check first name, last name, skills, education, work experience
		const key = search.toLowerCase()
		const filteredCandidates = candidates.filter(candidate => {
			const fullName = joinName(candidate).toLowerCase()
			const skills = candidate.skills?.map(skill => skill.name).join(' ').toLowerCase() || ''
			const education = candidate.education?.join(' ').toLowerCase() || ''
			const workExperience = candidate.work_experience?.join(' ').toLowerCase() || ''
			const certifications = candidate.certifications?.join(' ').toLowerCase() || ''
			return fullName.includes(key) || skills.includes(key) || education.includes(key) || workExperience.includes(key) || certifications.includes(key)
		})
		setCandidates(filteredCandidates)
	}

	// Filter by skills
	const filter = async (e) => {
		e.preventDefault()
		const key = e.target.value
		if (key === 'all') {
			// Reload page
			router.reload()
			return
		}
		// Candidate skill.name must include key
		const filteredCandidates = candidates.filter(candidate => {
			return candidate.skills?.some(skill => skill.name.toLowerCase().includes(key))
		})
		setCandidates(filteredCandidates)
	}

	// Save/Bookmark a candidate
	const bookmarkCandidate = async (candidateId) => {
		const res = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/candidate/bookmark?id=${candidateId}`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`,
			}
		})
		const data = await res.json()
		if (data?.error) {
			alert(data.error)
		} else if (data?.message) {
			alert('Bookmark removed')
		} else {
			alert('Candidate bookmarked')
		}
		// Reload page
		router.reload()
	}

	useEffect(() => {
		if (user && candidates?.length) {
			// Get candidate bookmarks
			const bookmarkedCandidates = async () => {
				const res = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/candidate/bookmark`, {
					method: 'GET',
					headers: {
						'Content-Type': 'application/json',
						Authorization: `Bearer ${token}`
					}
				})
				const bookmarks = await res.json()
				if (bookmarks?.length) {
					const updatedCandidates = candidates.map(candidate => {
						if (bookmarks.some(bookmark => bookmark.candidate_id === candidate.id)) {
							return { ...candidate, bookmarked: true }
						}
						return candidate
					})
					setCandidates(updatedCandidates)
					setBookmarksFetched(true)
				}
			}
			if (!bookmarksFetched) {
				bookmarkedCandidates()
			}
		}
	}, [user, candidates])

	const displaySavedCandidates = async () => {
		// Set jobs to only where bookmarked is true
		if (showingSaved) {
			// Reload page
			router.reload()
			return
		} else {
			setCandidates(candidates.filter(candidate => candidate.bookmarked))
			setShowingSaved(true)
		}
	}

	const inviteCandidate = async (e) => {
		e.preventDefault()
		const res = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/candidate/invite`, {
			method: 'POST',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`,
			},
			body: JSON.stringify(inviteForm)
		})
		const data = await res.json()
		if (data?.error) {
			alert(data.error)
		} else {
			alert('Candidate invited')
		}
		// Set showInviteForm to 0
		setShowInviteForm(0)
	}

	return (
		<>
			<Header />
			<main className={styles.jobsPage}>
				<div className="container">
					<div className={styles.title}>
						<h1>Browse all jobs</h1>
						{user && !showingSaved ? <button type="button" onClick={displaySavedCandidates}>View bookmarked candidates</button> : null}
						{user && showingSaved ? <button type="button" onClick={displaySavedCandidates}>View all candidates</button> : null}
					</div>

					{/* Search */}
					<form className={styles.search} onSubmit={searchJobs}>
						<input type="text" placeholder="Search jobs" onChange={(e) => setSearch(e.target.value)} />
						<button type="submit">Search</button>
					</form>

					{/* Filters */}
					<div className={styles.filters}>
						<div className={styles.filter}>
							<label htmlFor="skills">Skills</label>
							<select name="skills" id="skills" onChange={(e) => filter(e)}>
								<option value="all">All</option>
								{skills?.length ? skills.map(skill => (
									<option key={skill.id} value={skill.name}>{skill.name.toUpperCase()}</option>
								)) : null}
							</select>
						</div>
					</div>

					<div className={styles.jobs}>
						{candidates?.length ? candidates.map(candidate => (
							<div key={candidate.id} className={styles.job}>
								<div>
									<h2 className={styles.jobTitle}>{joinName(candidate)}</h2>
									<div className={styles.links}>
										{candidate.linkedin_url ? <Link href={candidate.linkedin_url} target="_blank" rel="noopener noreferrer" className={styles.linkedin}>View LinkedIn</Link> : null}
										{candidate.github_url ? <Link href={candidate.github_url} target="_blank" rel="noopener noreferrer" className={styles.github}>View GitHub</Link> : null}
										<Link href={`/candidate/${candidate.id}`} className={styles.viewProfile}>View profile</Link>
									</div>
									{/* Candidate skills */}
									{candidate.skills?.length ?
										<ul className={styles.jobMeta}>
											{candidate.skills.map(skill => (
												<li key={skill.id} className={styles.jobMetaItem}>{skill.name}</li>
											))}
										</ul>
									: null}
								</div>
								<div className={styles.jobActions}>
									{/* Bookmark candidate */}
									{candidate.bookmarked ?
										<button type="button" className={styles.saveJob} onClick={() => bookmarkCandidate(candidate.id)}>Remove bookmark</button>
										:
										<button type="button" className={styles.saveJob} onClick={() => bookmarkCandidate(candidate.id)}>Bookmark</button>
									}
									{/* Invite to job */}
									<button type="button" className={styles.saveJob} onClick={() => setShowInviteForm(candidate.id)}>Invite to job</button>
								</div>
								{/* Invite form */}
								{showInviteForm === candidate.id ?
									<form className={styles.inviteForm} onSubmit={(e) => inviteCandidate(e, candidate.id)}>
										<label htmlFor="job">Job</label>
										<select name="job" id="job" onChange={(e) => setInviteForm({ candidate_id: candidate.id, job_id: e.target.value })}>
											<option value="">Select a job</option>
											{user?.job_posts?.length ? user.job_posts.map(job => (
												<option key={job.id} value={job.id}>{job.title}</option>
											)) : null}
										</select>
										<button type="submit" className={styles.saveJob}>Invite</button>
									</form>
								: null}
							</div>
						)) : <p>No candidates found</p>}
					</div>
				</div>
			</main>
		</>
	)
}

export async function getServerSideProps() {
	// Get all skills
	const skillRes = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/api/browse_candidates/allcandidateskills`)
	const skills = await skillRes.json()

	return {
		props: {
			skills
		},
	}
}

export default Candidates