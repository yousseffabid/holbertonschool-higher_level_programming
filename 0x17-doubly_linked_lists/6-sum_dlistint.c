#include "lists.h"
/**
 * sum_dlistint - sum of all data in the list
 * @h: pointer to  head of list
 * Return: int sum of all data
 */
int sum_dlistint(dlistint_t *head)
{
	int sum;

	if (head == NULL)
		return (0);

	sum = 0;
	while (head)
	{
		sum += head->n;
		head = head->next;
	}
	return (sum);
}
