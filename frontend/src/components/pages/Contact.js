import React, { useState, useEffect } from 'react';
import PropTypes from 'prop-types'

import ReCAPTCHA from "react-google-recaptcha";

import { connect } from 'react-redux';
import { addInquiry } from '../../actions/pages';

const Contact = ({
  auth: { userLoading, user },
  pages: { contacting },
  addInquiry
}) => {

  const [name, setName] = useState(user? user.first_name+' '+user.last_name : '');
  const [email, setEmail] = useState(user? user.email : '');
  const [phone, setPhone] = useState(user? user.contact ? user.contact : '' : '');
  const [subject, setSubject] = useState('');
  const [message, setMessage] = useState('');
  const [captchaValid, setCaptchaValid] = useState(false);

  useEffect(() => {
    if (!userLoading) {
      M.updateTextFields();
      $('#id_message').characterCounter();
    }
  }, [userLoading]);

  useEffect(() => {
    if (!contacting) { 
      $('.loader').fadeOut()
    } else {
      $('.loader').show()
    }
  }, [contacting]);

  const onSubmit = async e => {
    e.preventDefault();

    if (!name || !email || !phone || !message) {
      M.toast({
        html: 'Please fill in required fields',
        displayLength: 5000,
        classes: 'red'
      });
    } else if(!captchaValid) {
      M.toast({
        html: 'Please check captcha box',
        displayLength: 5000,
        classes: 'red'
      });
    } else {
      addInquiry({
        name,
        email,
        phone,
        subject,
        message,
        contact_type: 'question'
      });
      setName('')
      setEmail('')
      setPhone('')
      setSubject('')
      setMessage('')
    }
  }

  return (
    <section className="section section-contact">
      <div className="container">
        <div className="row">
          <div className="col s12">
            <h4 className="contact-title">Send us a Message</h4>
          </div>
        </div>
        <div className="row">
          {!userLoading ? (
            <form method="POST" onSubmit={onSubmit} noValidate>
              <div className="col s12 m4 l4">
                <div className="input-field">
                  <label htmlFor="id_name">Name</label>
                  <input type="text" name="name" rows="1" value={name} maxLength="50" className="form-control" id="id_name" onChange={e => setName(e.target.value)} required/>
                </div>
              </div>
              <div className="col s12 m4 l4">
                <div className="input-field">
                  <label htmlFor="id_email">Email</label>
                  <input type="text" name="email" rows="1" value={email} maxLength="50" className="form-control" id="id_email" onChange={e => setEmail(e.target.value)} required/>
                </div>
              </div>
              <div className="col s12 m4 l4">
                <div className="input-field">
                  <label htmlFor="id_phone">Phone</label>
                  <input type="text" name="phone" rows="1" value={phone} maxLength="50" className="form-control" id="id_phone" onChange={e => setPhone(e.target.value)} required/>
                </div>
              </div>
              <div className="col s12">
                <div className="input-field">
                  <label htmlFor="id_subject">Subject</label>
                  <input type="text" name="subject" rows="1" maxLength="200" value={subject} className="form-control " id="id_subject" onChange={e => setSubject(e.target.value)}/>
                </div>
              </div>
              <div className="col s12">
                <div className="input-field">
                  <label htmlFor="id_message">Message</label>
                  <textarea id="id_message" name="message" data-length="1500" cols="40" rows="10" value={message} maxLength="4000" className="materialize-textarea grey-text text-darken-2" onChange={e => setMessage(e.target.value)} required></textarea>
                </div>
              </div>
              <div className="col s12 flex-col center mb-4">
                <div id="google-captcha-group" className="col center">
                  <ReCAPTCHA
                    sitekey="6LdGa-IZAAAAAPhgbM7qWDb7iBSJbr9z23yGcGgE"
                    onChange={() => setCaptchaValid(true)}
                  />
                </div>
              </div>
              <button type="submit" className="btn btn-large btn-extended green mt-5 mb-5">Send Message</button>
            </form>
          ) : undefined}
        </div>
      </div>
    </section>
  )
}

Contact.propTypes = {
  addInquiry: PropTypes.func.isRequired,
}

const mapStateToProps = state => ({
  auth: state.auth,
  pages: state.pages
});

export default connect(mapStateToProps, { addInquiry })(Contact);
