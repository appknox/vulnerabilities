
Automated tools find it hard to understand context, hence it's up to a
person to perform these kinds of tests. The following two examples will
illustrate how understanding the functionality of the application, the
developer's intentions, and some creative "out-of-the-box" thinking can
break the application's logic. The first example starts with a
simplistic parameter manipulation, whereas the second is a real world
example of a multi-step process leading to completely subvert the
application.

Example 1: Suppose an e-commerce site allows users to select items to purchase,
view a summary page and then tender the sale. What if an attacker was
able to go back to the summary page, maintaining their same valid
session and inject a lower cost for an item and complete the
transaction, and then check out?

Example 2: Holding/locking resources and keeping others from purchases these items
online may result in attackers purchasing items at a lower price. The
countermeasure to this problem is to implement timeouts and mechanisms
to ensure that only the correct price can be charged.

Example 3: What if a user was able to start a transaction linked to their
club/loyalty account and then after points have been added to their
account cancel out of the transaction? Will the points/credits still be
applied to their account?
