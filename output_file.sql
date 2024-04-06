--
-- PostgreSQL database dump
--

-- Dumped from database version 16.2
-- Dumped by pg_dump version 16.2

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: student_info; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_info (
    rollno character varying(20) NOT NULL,
    student_name character varying(50),
    class character varying(20)
);


ALTER TABLE public.student_info OWNER TO postgres;

--
-- Name: student_login; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_login (
    rollno character varying(20) NOT NULL,
    email character varying(100) NOT NULL,
    password character varying(255) NOT NULL
);


ALTER TABLE public.student_login OWNER TO postgres;

--
-- Name: student_subject; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.student_subject (
    rollno character varying(20) NOT NULL,
    subject character varying(20) NOT NULL,
    total_classes integer,
    attended_class integer
);


ALTER TABLE public.student_subject OWNER TO postgres;

--
-- Name: subject_videos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.subject_videos (
    teacher_id character varying(30) NOT NULL,
    sub_name character varying(30) NOT NULL
);


ALTER TABLE public.subject_videos OWNER TO postgres;

--
-- Name: teacher_login; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.teacher_login (
    sno character varying(20) NOT NULL,
    email character varying(100) NOT NULL,
    password character varying(255) NOT NULL
);


ALTER TABLE public.teacher_login OWNER TO postgres;

--
-- Name: videos; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.videos (
    subject_name character varying(30) NOT NULL,
    link character varying(500)
);


ALTER TABLE public.videos OWNER TO postgres;

--
-- Data for Name: student_info; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_info (rollno, student_name, class) FROM stdin;
\.


--
-- Data for Name: student_login; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_login (rollno, email, password) FROM stdin;
\.


--
-- Data for Name: student_subject; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.student_subject (rollno, subject, total_classes, attended_class) FROM stdin;
\.


--
-- Data for Name: subject_videos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.subject_videos (teacher_id, sub_name) FROM stdin;
\.


--
-- Data for Name: teacher_login; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.teacher_login (sno, email, password) FROM stdin;
\.


--
-- Data for Name: videos; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.videos (subject_name, link) FROM stdin;
\.


--
-- Name: student_info student_info_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_info
    ADD CONSTRAINT student_info_pkey PRIMARY KEY (rollno);


--
-- Name: student_login student_login_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_login
    ADD CONSTRAINT student_login_email_key UNIQUE (email);


--
-- Name: student_login student_login_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_login
    ADD CONSTRAINT student_login_pkey PRIMARY KEY (rollno);


--
-- Name: student_subject student_subject_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_subject
    ADD CONSTRAINT student_subject_pkey PRIMARY KEY (rollno, subject);


--
-- Name: subject_videos subject_videos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subject_videos
    ADD CONSTRAINT subject_videos_pkey PRIMARY KEY (teacher_id, sub_name);


--
-- Name: teacher_login teacher_login_email_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher_login
    ADD CONSTRAINT teacher_login_email_key UNIQUE (email);


--
-- Name: teacher_login teacher_login_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.teacher_login
    ADD CONSTRAINT teacher_login_pkey PRIMARY KEY (sno);


--
-- Name: videos videos_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.videos
    ADD CONSTRAINT videos_pkey PRIMARY KEY (subject_name);


--
-- Name: student_info student_info_rollno_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_info
    ADD CONSTRAINT student_info_rollno_fkey FOREIGN KEY (rollno) REFERENCES public.student_login(rollno);


--
-- Name: student_subject student_subject_rollno_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.student_subject
    ADD CONSTRAINT student_subject_rollno_fkey FOREIGN KEY (rollno) REFERENCES public.student_info(rollno);


--
-- Name: subject_videos subject_videos_teacher_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.subject_videos
    ADD CONSTRAINT subject_videos_teacher_id_fkey FOREIGN KEY (teacher_id) REFERENCES public.teacher_login(sno);


--
-- PostgreSQL database dump complete
--

