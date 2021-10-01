package com.DBdesc;

import java.util.Date;

@Entity

@Table
 public class Compliance {

 @Id
 @GeneratedValue(strategy = GenerationType.IDENTITY)
 private int complianceID;
 private String rltype;
 private String details;
 private Date createDate;

 @ManyToOne
 @JoinColumn(name = "dept_id")
 private Department dept;

 public Compliance() {

 }
 public Compliance(String rltype, String details, Date createDate, Department dept) {
 super();
 this.rltype = rltype;
 this.details = details;
 this.createDate = createDate;
 this.dept = dept;
 }

 public Compliance(int complianceID, String rltype, String details, Date createDate,
Department dept) {
 super();
 this.complianceID = complianceID;
 this.rltype = rltype;
 this.details = details;
 this.createDate = createDate;
 this.dept = dept;
 }

 public void setComplianceID(int complianceID) {
 this.complianceID = complianceID;
 }
 public int getComplianceID() {
 return complianceID;
 }
 public String getRltype() {
 return rltype;
 }
 public void setRltype(String rltype) {
 this.rltype = rltype;
 }
 public String getDetails() {
 return details;
 }
 public void setDetails(String details) {
 this.details = details;
 }
 public Date getCreateDate() {
 return createDate;
 }
 public void setCreateDate(Date createDate) {
 this.createDate = createDate;
 }
 public Department getDept() {
 return dept;
 }
 public void setDept(Department dept) {
 this.dept = dept;
}



 }
