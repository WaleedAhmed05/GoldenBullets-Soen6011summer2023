import Header from '@/components/layout/Header'
import styles from '@/styles/Home.module.scss'
import Link from "next/link";

const Home = () => {
	return (
		<>
			<Header />
			<main>
			<div className={styles.hero}>
					{/*<h1>Concordia Career Services</h1>*/}
                <div className={styles.test}>
					<div className="styles.hero-video__wrap">
						<video autoPlay loop muted
							   poster="https://www.flowd.co.uk/wp-content/themes/flowd/img/video/flowd.jpg" id="bgvid">
							<source src="https://www.flowd.co.uk/wp-content/themes/flowd/img/video/flowd.webm"
									type="video/webm"/>

							<source src="https://www.flowd.co.uk/wp-content/themes/flowd/img/video/flowd.mp4"
									type="video/mp4">
							</source>
							<source src="https://www.flowd.co.uk/wp-content/themes/flowd/img/video/flowd.ogg"
										type="video/ogg"/>

						</video>
					</div>
				</div>
                <div className={styles.sheldonBg}>

				</div>
				<div className={styles.verticalLineonDiv}>

				</div>
				{/*<div>*/}
				{/*	cznbzdgjhdtgjlDTmjnk:LFDGN*/}
				{/*</div>*/}
				<div className={styles.textOnBg}>
					<div className={styles.homePageText}>
						<h3>Your Gateway to Successful Partnerships</h3>
						<h1>Connecting Talent and Opportunity	</h1>
						{/*<p>Sign up as an employer to post jobs</p>*/}
						{/*<Link href={`${process.env.NEXT_PUBLIC_API_URL}/auth/login?type=employer`} className={styles.googleLogin}>Signup/Login as an employer</Link>*/}
						<div className={styles.vSlidesWrap}>
							<div className={styles.vSlides}>
								<h2 className={styles.vSlide} >Unlock Your Potential</h2>
								{/*<h2>Concordia Career Services</h2>*/}
								{/*<h2></h2>*/}
							</div>
						</div>
					</div>
				</div>

				<div className={styles.test2}>
                    <div className={styles.titleAbout}>
						The Story <span>Behind Our</span> Vision
					</div>
					<div className={styles.ContainerAbout}>
						<div className={styles.aboutLine}>
							<div className={styles.aboutLineTitle}>
								{/*nastaran*/}
								<img src="https://drive.google.com/uc?id=1D022jl2QCnTl4llmNQ88FzXdebgT2jUA"
									 loading="lazy" alt="Nastaran&#x27;s picture" className="testimonial-image"/>
								<div>
									<h2 >Nastaran Naseri</h2>
									<div className={styles.aboutDesc}>Backend/Database</div>
									<p className={styles.aboutParagraph}>In charge of both the design and management of
										the platform's database architecture, in addition to developing the server-side
										logic and functionality.</p>
								</div>
							</div>
							<div className={styles.aboutLineTitle}>
								{/*dina*/}
								<img src="https://drive.google.com/uc?id=1Id2II3busOWuqXkCWID8Z73QUxvhJoWI"
									 loading="lazy" alt="Dina&#x27;s picture" className="testimonial-image"/>
								<div>
									<h2 >Dina Omidvar Tehrani</h2>
									<div className={styles.aboutDesc}>Frontend/Backend</div>
									<p className={styles.aboutParagraph}>Her expertise centers on the implementation of
										the platform's user interface and user experience (UI/UX) elements, in addition
										to her involvement in developing the server-side logic and functionality.</p>
								</div>
							</div>
						</div>
						<div className={styles.aboutLine}>
							<div className={styles.aboutLineTitle}>
								{/*sadman*/}
								<img src="https://drive.google.com/uc?id=1O7DxI_2UzRqRSnAxDBTdZTvpFZpR0nI8"
									 loading="lazy" alt="Sadman&#x27;s picture" className="testimonial-image"/>
								<div>
									<h2 >Sadman Shawmik Himalay</h2>
									<div className={styles.aboutDesc}>Frontend/Backend</div>
									<p className={styles.aboutParagraph}>Specializes in implementing the user interface
										and user experience (UI/UX) aspects of the platform as well as developing the
										server-side logic and functionality.</p>
								</div>
							</div>
							<div className={styles.aboutLineTitle}>
								{/*yungash*/}
								<img src="https://drive.google.com/uc?id=1cV_S6Ex6HboccnZD4sTs2eqfC6WZeTJD"
									 loading="lazy" alt="Yugansh&#x27;s picture" className="testimonial-image"/>
								<div>
									<h2 >Yugansh Goyal</h2>
									<div className={styles.aboutDesc}>Backend/Database</div>
									<p className={styles.aboutParagraph}>Focuses on developing the server-side logic and
										functionality. He also was responsible for designing and managing the database
										architecture of the platform.</p>
								</div>
							</div>
						</div>
						<div className={styles.aboutLine}>
							<div className={styles.aboutLineTitle}>
								{/*waleed*/}
								<img src="https://drive.google.com/uc?id=1WFDupf6HathcdVh96qAnzKxAS0kAqI3v"
									 loading="lazy" alt="Waleed&#x27;s picture" className="testimonial-image"/>
								<div>
									<h2 >Waleed Ahmed Siddiqui</h2>
									<div className={styles.aboutDesc}>Backend/Testing</div>
									<p className={styles.aboutParagraph}>In charge of testing and ensuring the quality
										and reliability of the platform by developing test plans and executing various
										testing methodologies. He also developes the server-side logic and functionality
										of the platform.</p>
								</div>
							</div>
							<div className={styles.aboutLineTitle}>
								{/*simon*/}
								<img src="https://drive.google.com/uc?id=1y9LpDRFwOCQa4MXfq69g5vl7G8BVocgu"
									 loading="lazy" alt="Ziran&#x27;s picture" className="testimonial-image"/>
								<div>
									<h2 >Ziran Cao</h2>
									<div className={styles.aboutDesc}>Backend/Database</div>
									<p className={styles.aboutParagraph}>His primary focus lies in the development of
										server-side logic and functionality, alongside being accountable for the design
										and management of the platform's database architecture.</p>
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

export default Home