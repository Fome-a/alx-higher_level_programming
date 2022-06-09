#include <stdio.h>
#include "lists.h"
/**
 * print_dlistint -  a function
 * head: the head of list
 * struct dlistint_t - temp node for traversing
 * Return: number element of the link list
 */

void print_dlistint(void)
{
	struct dlistint_t *temp;
	int no_elem = 0;

	if (head != Null)
	{
		temp = head;
		while (temp->next != null)
		{
			printf("%d \n", temp->n);
			no_elem++;
			temp = temp->next;
		}
	}
	return (no_elem);

}
