import { useState, useEffect } from 'react'
import { useAppContext } from '@/context/AppContext'
import Header from '@/components/layout/Header'
import styles from '@/styles/Notifications.module.scss'
import { formatDate } from '@/utils'

const Notifications = () => {
	const [notifications, setNotifications] = useState([])
	const { user, token } = useAppContext()

	useEffect(() => {
		if (user && token) {
			getNotifications()
		}
	}, [user, token])

	const getNotifications = async () => {
		const res = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/notifications`, {
			method: 'GET',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`
			}
		})
		const data = await res.json()
		if (res.ok) {
			// Sort notifications by created_at date
			data.sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
			setNotifications(data)
		}
	}

	const markAsRead = async (id) => {
		const res = await fetch(`${process.env.NEXT_PUBLIC_URL}/api/notifications/${id}`, {
			method: 'PUT',
			headers: {
				'Content-Type': 'application/json',
				Authorization: `Bearer ${token}`
			}
		})
		const data = await res.json()
		if (res.ok && data.success) {
			getNotifications()
		}
	}

	return (
		<>
			<Header />
			<main className={styles.notificationsPage}>
				<div className="container">
					{!user && (
						<div className="login">
							<p>Please login to view your notifications.</p>
						</div>
					)}
					{user ? (
						<>
							<h1>Notifications</h1>
							{notifications.length > 0 ? (
								<>
									<h2>Unread</h2>
									<ul className={styles.notificationsList}>
										{notifications.map(notification => {
											if (notification.status === 'unread') {
												return (
													<li key={notification.id} className={notification.status === 'read' ? styles.notificationDisabled : null}>
														<h3>
															<span className={styles.notificationDate}>{formatDate(notification.created_at)}</span>
															{notification.title}
														</h3>
														<div className={styles.notificationContent}>
															<p>{notification.body}</p>
															<button type="button" onClick={() => markAsRead(notification.id)}>Mark as read</button>
														</div>
													</li>
												)
											}
										})}
									</ul>

									<h2>Read</h2>
									<ul className={styles.notificationsList}>
										{notifications.map(notification => {
											if (notification.status === 'read') {
												return (
													<li key={notification.id} className={notification.status === 'read' ? styles.notificationDisabled : null}>
														<h3>
															<span className={styles.notificationDate}>{formatDate(notification.created_at)}</span>
															{notification.title}
														</h3>
														<div className={styles.notificationContent}>
															<p>{notification.body}</p>
															<button type="button" onClick={() => markAsRead(notification.id)}>Mark as read</button>
														</div>
													</li>
												)
											}
										})}
									</ul>
								</>
							) : (
								<p>No notifications</p>
							)}
						</>
					) : null}
				</div>
			</main>
		</>
	)
}

export default Notifications