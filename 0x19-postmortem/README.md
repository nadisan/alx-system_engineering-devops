postmortem: Database Outage on 2023-11-12

TL;DR: Our database took a nap for 30 minutes, but we're back up and running now. We're investigating the root cause and taking steps to prevent it from happening again.
![image](https://github.com/nadisan/alx-system_engineering-devops/assets/76504146/b742e321-a8c8-495c-9f5e-8cbea03675be)

What happened?

On 2023-11-12 at 11:00am PST, our database became unresponsive. This caused our application to be unavailable for 30 minutes, affecting 100% of our users.

What was the root cause?

We're still investigating the root cause of the outage, but we believe it was caused by a hardware failure on one of our database servers.

How did we fix it?

We failed over to our secondary database server and rebuilt the database. Once the database was rebuilt, users were able to access the application again.

What are we doing to prevent it from happening again?

We're taking the following steps to prevent similar outages from happening in the future:

    Replacing the failed hardware on the database server
    Reviewing our database monitoring alerts to make sure they're configured to trigger quickly for high CPU usage
    Implementing a load balancer to distribute traffic between multiple database servers
    Implementing a disaster recovery plan for the database

We know that database outages are no laughing matter, but we can't help but think that this one was caused by a particularly stubborn gremlin. We've sent our team of gremlin wranglers out to track him down and give him a good stern talking to.

![banish-gremlins1](https://github.com/nadisan/alx-system_engineering-devops/assets/76504146/4d412787-a98f-4dbe-917b-94720f0cd6c9)



Conclusion

We apologize for any inconvenience the database outage may have caused our users. We're committed to providing a reliable and stable service, and we're taking steps to prevent similar outages from happening in the future.

Thank you for your understanding.
