// import Header from '@/components/layout/Header';
// import ApplicationForm from '@/components/pages/job_apply/job_application_form';
// import styles from '@/styles/ApplicationForm.module.scss';
//
// const Apply = () => {
//   return (
//     <>
//       <Header />
//       <main className={styles.applyPage}>
//         <div className="container">
//           <h1>Job Application</h1>
//           <ApplicationForm />
//         </div>
//       </main>
//     </>
//   );
// };
//
// export default Apply;

// import { useState } from 'react';
// import { useRouter } from 'next/router';
import Header from '@/components/layout/Header';
import styles from '@/styles/ApplicationForm.module.scss';

import { prettifyJobType } from '@/utils';
import Link from 'next/link';

const ApplicationForm = () => {
  // const [firstName, setFirstName] = useState('');
  // const [lastName, setLastName] = useState('');
  // const [cv, setCv] = useState(null);
  // const [coverLetter, setCoverLetter] = useState(null);
  // const [email, setEmail] = useState('');
  // const [phone, setPhone] = useState('');

  //
  // const router = useRouter();
//

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const formData = new FormData();
      // formData.append('first_name', firstName);
      // formData.append('last_name', lastName);
      // formData.append('cv', cv);
      // formData.append('cover_letter', coverLetter);
      // formData.append('email', email);
      // formData.append('phone', phone);

      const response = await fetch('/api/apply', {
        method: 'POST',
        body: formData,
      });

      if (response.ok) {
        // Application submitted successfully
        // Perform any necessary actions (e.g., show success message, redirect, etc.)
        console.log('Application submitted successfully');
        // router.push('/success'); // Replace '/success' with your desired success page route

      } else {
        // Application submission failed
        // Handle the error (e.g., show error message)
        console.error('Application submission failed');
      }
    } catch (error) {
      // Error occurred during the API request
      // Handle the error (e.g., show error message)
      console.error('Error occurred during application submission:', error);
    }
  };

  return (
    <>
      <Header />
      <main className={styles.createJobPage}>
        <div className="container">
          <h1>Job Application Form</h1>
          <form onSubmit={handleSubmit} className={styles.createJobForm}>
            <div className={styles.formGroup}>
              <label htmlFor="firstName">First Name:</label>
              <input
                type="text"
                id="firstName"
                name="firstName"
                // value={firstName}
                onChange={(e) => setFirstName(e.target.value)}
                required
              />
            </div>
            <div className={styles.formGroup}>
              <label htmlFor="lastName">Last Name:</label>
              <input
                type="text"
                id="lastName"
                name="lastName"
                // value={lastName}
                onChange={(e) => setLastName(e.target.value)}
                required
              />
            </div>
            <div className={styles.formGroup}>
              <label htmlFor="cv">CV:</label>
              <input
                type="file"
                id="cv"
                name="cv"
                onChange={(e) => setCv(e.target.files[0])}
                required
              />
            </div>
            <div className={styles.formGroup}>
              <label htmlFor="coverLetter">Cover Letter:</label>
              <input
                type="file"
                id="coverLetter"
                name="coverLetter"
                onChange={(e) => setCoverLetter(e.target.files[0])}
                required
              />
            </div>
            <div className={styles.formGroup}>
              <label htmlFor="email">Email:</label>
              <input
                type="email"
                id="email"
                name="email"
                // value={email}
                onChange={(e) => setEmail(e.target.value)}
                required
              />
            </div>
            <div className={styles.formGroup}>
              <label htmlFor="phone">Phone:</label>
              <input
                type="text"
                id="phone"
                name="phone"
                // value={phone}
                onChange={(e) => setPhone(e.target.value)}
                required
              />
            </div>
            <div className={styles.formGroup}>
              <button type="submit" className="btn btn-primary">Submit Application</button>
            </div>
          </form>
        </div>
      </main>
    </>
  );
};

export default ApplicationForm;
