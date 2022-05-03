#include "lists.h"
/**
 * is_palindrome - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: 1 if plindrome or 0 if it is not
 */
int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *left, *right, *temp1, *temp2;

	if (head == NULL || (*head)->next == NULL)
		return (0);
	if (*head == NULL)
		return (1);

	fast = *head;
	slow = *head;

	while (fast && fast->next)
	{
		fast = fast->next->next;
		slow = slow->next;
	}

	temp1 = NULL;
	temp2 = NULL;
	while (slow)
	{
		temp2 = slow->next;
		slow->next = temp1;
		temp1 = slow;
		slow = temp2;
	}

	right = temp1;
	left = *head;
	while (right)
	{
		if (left->n != right->n)
			return (0);
		right = right->next;
		left = left->next;
	}
	return (1);
}
