import Link from 'next/link'
import Header from '@/components/layout/Header'
import styles from '@/styles/Login.module.scss'
import { useAppContext } from 'context/AppContext'
import { useRouter } from 'next/router'
import { useEffect } from 'react'

const Login = () => {
	const { user } = useAppContext()

	// If user is logged in, redirect to homepage
	const router = useRouter()
	
	useEffect(() => {
		if (user) {
			router.push('/')
		}
	}, [user])

	return (
		<>
			<Header />
			<main>
				<div className={styles.login}>
					<div className={styles.test}>
						<div className="styles.hero-video__wrap">
							<video autoPlay loop muted poster="https://www.flowd.co.uk/wp-content/themes/flowd/img/video/flowd.jpg" id="bgvid">
								<source src="https://www.flowd.co.uk/wp-content/themes/flowd/img/video/flowd.webm" type="video/webm" />
								<source src="https://www.flowd.co.uk/wp-content/themes/flowd/img/video/flowd.mp4" type="video/mp4" />
								<source src="https://www.flowd.co.uk/wp-content/themes/flowd/img/video/flowd.ogg" type="video/ogg"/>
							</video>
						</div>
						<div className={styles.sheldonBg}></div>
						<div className={styles.verticalLineonDiv}>
					</div>
					<div className={styles.textOnBg}>
						<div className={styles.loginEmployer}>
							<h3>Want to hire?</h3>
							<Link href={`${process.env.NEXT_PUBLIC_API_URL}/auth/login?type=employer`} className={styles.googleLogin}>Signup/Login as an employer</Link>
							<div className={styles.vSlidesWrap}>
								<div className={styles.vSlides}>
									<h2 className={styles.vSlide} >Post job listings and reach qualified candidates</h2>
								</div>
							</div>
						</div>
						<div className={styles.loginCandidate}>
							<h3>Looking for a job?</h3>
							<Link href={`${process.env.NEXT_PUBLIC_API_URL}/auth/login?type=candidate`} className={styles.googleLogin}>Signup/Login as a candidate</Link>
							<div className={styles.vSlidesWrap}>
								<div className={styles.vSlides}>
									<h2 className={styles.vSlide} >Apply to a wide range of job opportunities</h2>
								</div>
							</div>
						</div>
					</div>
                  </div>
	           </div>
			</main>
		</>
	)
}

export default Login